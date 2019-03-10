import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  vision: DS.belongsTo('vision'),
  image: DS.attr('string'),
  order: DS.attr('number'),
  problems: DS.hasMany('problem'),
  initiatives: DS.hasMany('initiative'),
  benefits: DS.hasMany('benefit'),
  projects: DS.hasMany('project')
})
