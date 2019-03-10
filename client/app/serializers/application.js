import DS from 'ember-data'
import { underscore } from '@ember/string'

export default DS.JSONAPISerializer.extend({
  keyForAttribute: function (key) {
    return underscore(key) // model attributes with underscores from the server are usually overriden by Ember dasherizing
  },
  keyForRelationship: function (key) {
    return underscore(key)
  }

  // serializeHasMany: function (snapshot, json, relationship) {
  //   // do not serialize readonly relationships, causes poor behaviour at the server
  //   if (relationship.options && relationship.options.readOnly) return
  //   this._super(...arguments)
  // }
})
