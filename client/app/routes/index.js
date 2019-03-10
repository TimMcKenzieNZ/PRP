import Route from '@ember/routing/route'

export default Route.extend({

  model () {
    return {

      programmes: this.store.query('programme', {})
    }
  }

})
