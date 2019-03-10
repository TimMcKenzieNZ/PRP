import Component from '@ember/component'
import moment from 'moment'
import { computed } from '@ember/object'

import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'

export default Component.extend({

  inProgress: WORK_STATUSES.IN_PROGRESS,

  overdue: WORK_STATUSES.OVERDUE,

  dueTime: computed('deliverable.endDate', function () {
    let end = moment(this.deliverable.endDate)
    return end.diff(moment(), 'weeks')
  }),

  deliverableNotOverdue: computed('dueTime', function () {
    return this.dueTime >= 0
  }),

  weeksFromCurrent: computed('dueTime', function () {
    if (this.dueTime === -1) {
      return 'Last week'
    } else if (this.dueTime < 0) {
      return Math.abs(this.dueTime) + ' weeks ago'
    } else if (this.dueTime === 0) {
      return 'This week'
    } else if (this.dueTime === 1) {
      return 'Next week'
    } else {
      return this.dueTime + ' weeks'
    }
  }),

  deliverableNotComplete: computed('deliverable.status', 'deliverable.progress', function () {
    return (!(this.deliverable.status === 'Complete' || this.deliverable.progress === 1))
  }),

  classNames: ['change-deliverables-deliverable'],

  statusColor: computed('status', function () {
    switch (this.deliverable.status) {
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

  // text: computed('text', 'status', function () {
  //   return {
  //     value: this.deliverable.name + ': ' + (100 * this.deliverable.progress) + '%',
  //     style: {
  //       position: 'absolute',
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

  updateCount: computed('deliverable.updates', function () {
    return this.deliverable.updates.length
  }),

  hasUpdates: computed('updateCount', function () {
    return this.updateCount > 0
  }),

  updateCountText: computed('updateCount', function () {
    return `${this.updateCount} comment${this.updateCount === 1 ? '' : 's'}`
  }),

  actions: {
    setDeliverable () {
      this.setDeliverable()
    }
  }
})
