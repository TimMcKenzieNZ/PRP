import Component from '@ember/component'
import { computed } from '@ember/object'
import DS from 'ember-data'
import ENV from '../config/environment'

import { ROLE_NAMES } from 'client/constants'

export default Component.extend({

  classNames: ['project-managers'],

  ROLE_NAMES,

  space: ' ',

  imageLink: computed(function () {
    return (ENV.host || '') + '/media/prp/teammembers/images/default.jpg'
  }),

  hasProjectManagerPromise: computed('roles', function () {
    const promise = this.roles.then((rolesData) => {
      let hasManager = false
      rolesData.forEach(function (role) {
        if (role.get('role') === ROLE_NAMES.PROJECT_MANAGER) {
          hasManager = true
        }
      })
      return hasManager
    })
    return DS.PromiseObject.create({ promise })
  })

})
