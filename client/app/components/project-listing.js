import Component from '@ember/component'
import { computed } from '@ember/object'
import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'
import ENV from '../config/environment'

export default Component.extend({

  classNames: ['project-listing'],

  statusColor: computed('status', function () {
    switch (this.project.status) {
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

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/goals/images/placeholder.jpg'
  }),

  from: computed('status', function () {
    return { color: this.statusColor }
  }),
  to: computed('status', function () {
    return { color: this.statusColor }
  }),
  trailColor: STATUS_COLORS.GREY,

  projectName: computed('name', function () {
    return this.name
  }),

  projectProgress: computed('barProgress', function () {
    return parseFloat(this.barProgress)
  }),

  // text: computed('text', 'status', function () {
  //   return {
  //     value: this.projectName + ': ' + (100 * this.projectProgress) + '%',
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
    'border-radius': '16px',
    transition: '.1s ease-in-out'
  },

  actions: {

    click () {
      this.setProject(this.project)
      this.hasSelectedProject()
    }
  }

})
