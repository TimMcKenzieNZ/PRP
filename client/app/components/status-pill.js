import Component from '@ember/component'
import { computed } from '@ember/object'
import { WORK_STATUSES, STATUS_COLORS } from 'client/constants'

export default Component.extend({
  tagName: '',
  statusColor: computed('status', function () {
    switch (this.status) {
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
  })
})
