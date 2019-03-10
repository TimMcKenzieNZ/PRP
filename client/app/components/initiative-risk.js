import Component from '@ember/component'

export default Component.extend({
  classNames: ['initiative-risk'],

  actions: {
    click () {
      this.setRisk(this.risk)
    }
  }

})
