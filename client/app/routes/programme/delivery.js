import Route from '@ember/routing/route'

export default Route.extend({

  model () {
    const goals = this.modelFor('programme').programme.goals
    const initiatives = []
    // iterate through each goal and each goal's projects, and each project's initatives and
    // add it's initiatives to the array if they arn't in there already
    goals.forEach(function (goal) {
      goal.projects.forEach(function (project) {
        project.initiatives.forEach(function (initiative) {
          if (initiatives.indexOf(initiative) === -1) {
            initiatives.push(initiative)
          }
        })
      })
    })
    return {
      initiatives: initiatives,
      slug: this.modelFor('programme').programme.slug
    }
  }
})
