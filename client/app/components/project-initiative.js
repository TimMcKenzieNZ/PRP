import Component from '@ember/component'
import { computed } from '@ember/object'
import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'
import { inject as service } from '@ember/service'

export default Component.extend({

  router: service(), // For use in using the route.transitionTo function

  classNames: ['project-initiative'],

  statusColor: computed('statusColor', function () {
    switch (this.initiative.status) {
      case WORK_STATUSES.NOT_STATRED:
        return STATUS_COLORS.GREY
      case WORK_STATUSES.IN_PROGRESS:
        return STATUS_COLORS.TEALGREEN
      case WORK_STATUSES.COMPLETE:
        return STATUS_COLORS.TEALGREEN
      case WORK_STATUSES.OVERDUE:
        return STATUS_COLORS.ORANGE
      case WORK_STATUSES.BLOCKED:
        return STATUS_COLORS.RED
      case WORK_STATUSES.DEFERRED:
        return STATUS_COLORS.RED
      case WORK_STATUSES.CANCELLED:
        return STATUS_COLORS.BLUE
      case WORK_STATUSES.DELAYED:
        return STATUS_COLORS.ORANGE
      default:
        return STATUS_COLORS.BLACK
    }
  }),

  from: computed('status', function () {
    return { color: this.statusColor }
  }),
  to: computed('status', function () {
    return { color: this.statusColor }
  }),
  trailColor: STATUS_COLORS.GREY,

  initiativeName: computed('name', function () {
    return this.name
  }),

  initiativeProgress: computed('barProgress', function () {
    return parseFloat(this.barProgress)
  }),

  step (state, bar) {
    bar.stop()
    return bar.path.setAttribute('stroke', state.color)
  },

  svgStyle: {
    height: '8px',
    width: '100%',
    'border-radius': '4px'
  },

  actions: {
    loadInitiative (id) {
      this.get('router').transitionTo('programme.delivery.initiative', this.slug, id)
    }

  }

})
