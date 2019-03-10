import Component from '@ember/component'
import { set } from '@ember/object'

export default Component.extend({
  classNames: ['l-content-page'],

  selectedBenefitIds: [],
  selectedGoalIds: [],

  actions: {

    /**
     * Sets the highlighted goal & benefits when a goal is clicked on in the GUI
     * @param {*} goal A programme goal object
     */
    setGoal: function (goal) {
      if (goal != null) {
        set(this, 'selectedBenefitIds', goal.projects.map(b => b.id))
        set(this, 'selectedGoalIds', [goal.id])
      } else {
        set(this, 'selectedBenefitIds', [])
        set(this, 'selectedGoalIds', [])
      }
    }
  }

})
