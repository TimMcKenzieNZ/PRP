import Route from '@ember/routing/route'

export default Route.extend({

  selectedDeliverable: null,

  beforeModel: function (transition) {
    // pulling the given deliverable id from the query parameters given (if it exists)
    this.selectedDeliverable = transition.queryParams.deliverable
  },
  model () {
    const goals = this.modelFor('programme').programme.goals
    const deliverables = []
    // iterate through each goal and each goal's projects, and each project's initatives and
    // each initiative's deliverables and add them to the array if they arn't in there already
    goals.forEach(function (goal) {
      goal.projects.forEach(function (project) {
        project.initiatives.forEach(function (initiative) {
          initiative.deliverables.forEach(function (deliverable) {
            if (deliverables.indexOf(deliverable) === -1) {
              deliverables.push(deliverable)
            }
          })
        })
      })
    })
    // sort deliverables by end date decesending
    deliverables.sort((a, b) => (a.endDate > b.endDate) ? 1 : ((b.endDate > a.endDate) ? -1 : 0))
    return {
      deliverables: deliverables,
      selectedDeliverable: this.selectedDeliverable
    }
  }
})
