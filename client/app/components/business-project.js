import Component from '@ember/component'
import { set } from '@ember/object'

export default Component.extend({
  classNames: ['l-content-page'],

  selectedProject: null,

  hasSelectedProject: false,

  actions: {
    setProject: function (project) {
      set(this, 'selectedProject', project)
    },

    hasSelectedProject () {
      set(this, 'hasSelectedProject', true)
    }

  }
})
