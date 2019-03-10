import Component from '@ember/component'
import { computed } from '@ember/object'
import { IMPACT_VALUES, STATUS_COLORS } from 'client/constants'

export default Component.extend({
  tagName: '',
  impactColor: computed('impact', function () {
    switch (this.impact) {
      case IMPACT_VALUES.NO_IMPACT:
        return STATUS_COLORS.TEALGREEN
      case IMPACT_VALUES.LOW_IMPACT:
        return STATUS_COLORS.TEALGREEN
      case IMPACT_VALUES.MODERATE_IMPACT:
        return STATUS_COLORS.ORANGE
      case IMPACT_VALUES.SEVERE_IMPACT:
        return STATUS_COLORS.RED
      default:
        return STATUS_COLORS.GREY
    }
  })
})
