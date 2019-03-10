#!/usr/bin/env bash

# more bash-friendly output for jq
JQ="jq --raw-output --exit-status"

configure_aws_cli() {
  aws --version
  aws configure set default.region "$AWS_DEFAULT_REGION"
  aws configure set default.output json
}

set_env() {

  if [ "$CIRCLE_BRANCH" == "master" ]; then
    environment="uat"
  else
    echo "Unknown branch"
    exit 1
  fi
}

# Setting in aws, the cluster service task definition name ( the aws json is pulled and replaces the image tag with new tag of what we just built)
get_task_def() {
  task_def_name="${environment}-programme-reporting-prototype-task"
  task_def=$(aws ecs describe-task-definition --task-definition "$task_def_name")
  image="$ECR_ENDPOINT/$ECR_REPOSITORY:$CIRCLE_BUILD_NUM"
  # Pull and replace the aws json
  new_def=$(echo "$task_def" | $JQ --arg image "$image" ".taskDefinition.containerDefinitions[0].image=\$image | .taskDefinition | {family: .family, volumes: .volumes, containerDefinitions: .containerDefinitions}")
}

# Update the service to use new task definition
register_definition() {
  if new_task_def=$(aws ecs register-task-definition --cli-input-json "$new_def" | $JQ '.taskDefinition.taskDefinitionArn'); then
    echo "Revision: $new_task_def"
  else
    echo "Failed to register task definition"
    exit 1
  fi
}

update_service() {
  service_name="${environment}-programme-reporting-prototype-service"
  if update_service=$(aws ecs update-service --cluster "$environment" --service "$service_name" --task-definition "$new_task_def"); then
    echo "Updated service"
  else
    echo "Failed to update service"
    exit 1
  fi
}

configure_aws_cli
set_env
get_task_def
register_definition
update_service

exit 0
