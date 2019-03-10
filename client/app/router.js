import EmberRouter from '@ember/routing/router'
import config from './config/environment'

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
})

Router.map(function () {
  this.route('index', { path: '/' })
  this.route('programme', { path: '/:programmeSlug' }, function () {
    this.route('priorities')
    this.route('delivery', function () { // nesting routes for loading subcontent in a page, in this case specific initiatives
      this.route('initiative', { path: '/:initiativeID' })
    })
    this.route('change')
    this.route('benefits')
    this.route('dashboard')
  })
})

export default Router
