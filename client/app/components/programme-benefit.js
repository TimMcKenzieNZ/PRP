import Component from '@ember/component'
import ENV from '../config/environment'
import { computed } from '@ember/object'

export default Component.extend({
  // References for the CSS styling to highlight a benefit when the relevant goal is clicked
  classNames: ['programme-benefit'],
  classNameBindings: ['highlight:illuminated'],

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/placeholder.jpg'
  })

})
