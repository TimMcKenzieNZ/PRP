import Component from '@ember/component'
import { computed } from '@ember/object'
import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'

export default Component.extend({

  classNames: ['programme-initiatives'],

  statusColor: computed('status', function () {
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

  // text: computed('text', 'status', function () {
  //   return {
  //     value: this.initiativeName + ': ' + (100 * this.initiativeProgress) + '%',
  //     style: {
  //       position: 'absolute',
  //
  //       left: '3%',
  //       top: '16%',
  //       padding: 0,
  //       margin: 0
  //     }
  //   }
  // }),

  step (state, bar) {
    bar.stop()
    return bar.path.setAttribute('stroke', state.color)
  },

  svgStyle: {
    height: '16px',
    width: '100%',
    'border-radius': '8px'
  },

  actions: {

    click () {
      this.setInitiative(this.initiative)
      this.hasSelectedInitiative()
    }
  }

})
