import Component from '@ember/component'
import { set } from '@ember/object'

export default Component.extend({
  classNames: ['l-content-page'],

  init () {
    this._super(...arguments)
    // If the user has selected a deliverable from the delivery page, we open its status messages
    if (this.selectedDeliverable != null) {
      this.selectedDeliverableIds.push(this.selectedDeliverable)
    }
  },

  selectedDeliverableIds: [],

  actions: {
    setDeliverable: function (deliverable) {
      if (!this.selectedDeliverableIds.includes(deliverable.id)) {
        set(this, 'selectedDeliverableIds', this.selectedDeliverableIds.concat(deliverable.id))
      } else {
        this.selectedDeliverableIds.splice(this.selectedDeliverableIds.indexOf(deliverable.id), 1)
        set(this, 'selectedDeliverableIds', this.selectedDeliverableIds.concat())
      }
    }
  }
})
