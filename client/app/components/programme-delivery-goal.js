import Component from '@ember/component'
import ENV from '../config/environment'
import { computed } from '@ember/object'

export default Component.extend({
  isSelected: false,

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/placeholder.jpg'
  }),

  actions: {

    /**
     * Toggles a goal selection on and off
     */
    click () {
      if (!this.isSelected) {
        this.toggleProperty('isSelected')
        this.setGoal(this.goal)
      } else {
        this.toggleProperty('isSelected')
        this.setGoal(null)
      }
    }
  }

})
