import Route from '@ember/routing/route'
import RSVP from 'rsvp'

export default Route.extend({

  model ({ programmeSlug }) {
    return RSVP.hash({
      programme: this.store.query('programme', {
        filter: {
          'slug': programmeSlug
        },
        include: [
          'goals',
          'goals.projects',
          'goals.benefits',
          'goals.projects.initiatives',
          'goals.projects.roles.team_members',
          'goals.projects.initiatives.deliverables',
          'goals.projects.initiatives.risks',
          'goals.projects.initiatives.deliverables.updates'
        ].join(',')

      }).then(programmes => programmes.firstObject) // short hand for returning the promise hash
    })
  }
})
