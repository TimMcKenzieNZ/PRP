import Route from '@ember/routing/route'

export default Route.extend({

  model () {
    const goals = this.modelFor('programme').programme.goals
    const projects = []
    // iterate through each goal and add it's projects to the array if they arn't in there already
    goals.forEach(function (goal) {
      goal.projects.forEach(function (project) {
        if (projects.indexOf(project) === -1) {
          projects.push(project)
        }
      })
    })
    return {
      goals: goals,
      projects: projects
    }
  }
})
