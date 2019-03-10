import Component from '@ember/component'
import { computed } from '@ember/object'
import moment from 'moment'

export default Component.extend({
  tagName: 'span',

  date: computed('update.date', function () {
    return moment(this.update.date).fromNow()
  })

})
