import Route from '@ember/routing/route'

export default Route.extend({
  model () {
    const goals = this.modelFor('programme').programme.goals
    const projects = []
    // iterate through each goal and each goal's projects, add it' to the array if it isn't in there already
    goals.forEach(function (goal) {
      goal.projects.forEach(function (project) {
        if (projects.indexOf(project) === -1) {
          projects.push(project)
        }
      })
    })
    return {
      projects: projects,
      slug: this.modelFor('programme').programme.slug
    }
  }
})
