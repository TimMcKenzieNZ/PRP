import Component from '@ember/component'
import ENV from '../config/environment'

export default Component.extend({
  classNames: ['c-dashboard-vision'],
  dashboardImage: (ENV.host || '') + '/media/prp/default/uc-logo.png'
})
