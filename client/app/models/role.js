import DS from 'ember-data'

export default DS.Model.extend({
  role: DS.attr('string'),
  teamMembers: DS.hasMany('teammember')
})
