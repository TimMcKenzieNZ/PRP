import Component from '@ember/component'
import { computed } from '@ember/object'
import ENV from '../config/environment'
import moment from 'moment'

export default Component.extend({

  classNames: ['change-deliverable-status'],

  space: ' ',

  date: computed('update.date', function () {
    return moment(this.update.date, 'MM/DD/YYYY').toDate()
  }),

  updates: computed('deliverable.updates', function () {
    let updates = []
    this.deliverable.updates.forEach(function (update) {
      updates.push(update)
    })
    return updates.sort(function (a, b) {
      a = new Date(a.date)
      b = new Date(b.date)
      return a > b ? -1 : a < b ? 1 : 0
    })
  }),

  display: computed('hasSelectedDeliverable', function () {
    return this.hasSelectedDeliverable
  }),

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/teammembers/images/default.jpg'
  })

})
