import Component from '@ember/component'

import { PERSPECTIVES } from 'client/constants'

export default Component.extend({
  classNames: ['c-dashboard-perspectives'],
  perspectives: PERSPECTIVES
})
