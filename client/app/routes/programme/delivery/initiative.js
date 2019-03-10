import Route from '@ember/routing/route'

export default Route.extend({
  model ({ initiativeID }) {
    // retrieving the parent array of all initiatives
    const deliveryModel = this.modelFor('programme.delivery')
    let model = {
      initiatives: deliveryModel.initiatives
    }
    // retrieving the current initiative being looked at
    deliveryModel.initiatives.forEach(function (initiative) {
      if (initiative.get('id') === initiativeID) {
        model.initiative = initiative
      }
    })
    return model
  }
})
