import Component from '@ember/component'
import { computed } from '@ember/object'
import ENV from '../config/environment'

export default Component.extend({
  classNames: ['project-statistics'],

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/placeholder.jpg'
  }),

  warningImageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/warning.jpg'
  })

})
