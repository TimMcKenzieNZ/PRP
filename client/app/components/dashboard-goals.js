import Component from '@ember/component'
import ENV from '../config/environment'
import { computed } from '@ember/object'

export default Component.extend({
  classNames: ['c-dashboard-goals'],
  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/placeholder.jpg'
  })
})
