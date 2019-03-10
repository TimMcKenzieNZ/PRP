import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  endDate: DS.attr('date'),
  progress: DS.attr('number'),
  status: DS.attr('string'),
  order: DS.attr('number'),
  statusMessage: DS.attr('string'),
  teamImpact: DS.attr('string'),
  sponsorImpact: DS.attr('string'),
  pmImpact: DS.attr('string'),
  updates: DS.hasMany('update'),
  initiative: DS.belongsTo('initiative')
})
