import Component from '@ember/component'
import { set } from '@ember/object'

export default Component.extend({
  classNames: ['initiative-statistics'],

  selectedRiskIds: [],

  actions: {
    setRisk: function (risk) {
      if (!this.selectedRiskIds.includes(risk.id)) {
        set(this, 'selectedRiskIds', this.selectedRiskIds.concat(risk.id))
      } else {
        this.selectedRiskIds.splice(this.selectedRiskIds.indexOf(risk.id), 1)
        set(this, 'selectedRiskIds', this.selectedRiskIds.concat())
      }
    }
  }
})
