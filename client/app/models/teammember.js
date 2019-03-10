import DS from 'ember-data'

export default DS.Model.extend({
  firstName: DS.attr('string'),
  lastName: DS.attr('string'),
  position: DS.attr('string'),
  email: DS.attr('string'),
  image: DS.attr('string'),
  contactNumber: DS.attr('string'),
  roles: DS.hasMany('role'),
  updates: DS.hasMany('update')
})
