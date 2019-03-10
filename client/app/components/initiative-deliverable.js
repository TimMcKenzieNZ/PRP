import Component from '@ember/component'
import { computed } from '@ember/object'
import { inject as service } from '@ember/service'
import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'

export default Component.extend({

  router: service(),

  classNames: ['initiative-deliverable'],

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

  from: computed('statusColor', function () {
    return { color: this.statusColor }
  }),
  to: computed('statusColor', function () {
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
    height: '8px',
    width: '100%',
    'border-radius': '4px'
  },

  actions: {
    loadDeliverable (id) {
      this.get('router').transitionTo('programme.change', { queryParams: { programmeSlug: this.slug, deliverable: id } })
    }
  }

})
