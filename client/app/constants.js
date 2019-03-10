exports.ROLE_NAMES = {
  PROJECT_MANAGER: 'Project Manager'
}

exports.WORK_STATUSES = {
  NOT_STARTED: 'Not Started',
  IN_PROGRESS: 'In Progress',
  COMPLETE: 'Complete',
  OVERDUE: 'Overdue',
  BLOCKED: 'Blocked',
  DEFERRED: 'Deferred',
  CANCELLED: 'Cancelled',
  DELAYED: 'Delayed'
}

exports.STATUS_COLORS = {
  LIGHTGREEN: '#BCF5A9',
  TEALGREEN: '#00AA6E',
  GREY: '#ddd',
  BLUE: '#0080FF',
  RED: '#FF0000',
  ORANGE: '#F77223',
  BLACK: '#000000'
}

exports.CONVERSION_VALUES = {
  FLOATTOPERCENTAGE: 100
}

exports.DATETIME_VALUES = {
  CURRENTDATE: new Date().toDateString().substring(4, new Date().toDateString().length),
  CURRENTTIME: new Date(new Date().toDateString().substring(4, new Date().toDateString().length)).getTime()
}

exports.IMPACT_VALUES = {
  NO_IMPACT: 'none',
  LOW_IMPACT: 'low',
  MODERATE_IMPACT: 'moderate',
  SEVERE_IMPACT: 'severe'
}

exports.PERSPECTIVES = [
  { name: 'Priority', icon: 'flag', link: 'programme.priorities', id: 'priority' },
  { name: 'Delivery', icon: 'parcel', link: 'programme.delivery', id: 'delivery' },
  { name: 'Change', icon: 'change', link: 'programme.change', id: 'change' },
  { name: 'Alignment', icon: 'alignment', link: 'programme.benefits', id: 'benefit' }
]
