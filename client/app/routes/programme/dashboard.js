import Route from '@ember/routing/route'

export default Route.extend({

  model () {
    const model = this.modelFor('programme').programme
    return model
  }

})
