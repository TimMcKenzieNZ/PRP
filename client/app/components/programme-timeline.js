import Component from '@ember/component'
import d3 from 'd3'
import Ember from 'ember'
const { $ } = Ember

const getTickValues = (s, e, w) => {
  if (w < 600) return [s, e]
  const tickValues = []
  const durationMs = e.getTime() - s.getTime()
  const count = 5
  const intervalMs = durationMs / (count - 1)
  for (let i = 0; i < count; i++) {
    tickValues.push(new Date(s.getTime() + (intervalMs * i)))
  }
  return tickValues
}

const Timeline = (element, componentClass) => {
  const container = element.querySelector(`.${componentClass}`)

  const width = container.getBoundingClientRect().width
  const height = 160

  const strokeWidth = 2
  const arrowWidth = 7 // Note scaled by strokeWidth

  const svgContainer = d3
    .select(container)
    .append('svg')
    .attr('height', height)
    .attr('width', width)

  // End arrow marker definition
  svgContainer
    .append('defs')
    .append('marker')
    .attr('id', `${componentClass}__arrow-marker-end`)
    .attr('orient', 'auto')
    .attr('markerWidth', arrowWidth)
    .attr('markerHeight', arrowWidth)
    .attr('refX', 0)
    .attr('refY', arrowWidth / 2)
    .append('path')
    .attr('class', `${componentClass}__future-line-arrow`)
    .attr('d', `M0,0 V${arrowWidth} L${arrowWidth},${arrowWidth / 2} Z`)

  // The past timeline
  svgContainer
    .append('line')
    .attr('class', `${componentClass}__past-line`)
    .attr('stroke-width', strokeWidth)

  // The future timeline
  svgContainer
    .append('line')
    .attr('class', `${componentClass}__future-line`)
    .attr('stroke-dasharray', `${strokeWidth * 1.5} ${strokeWidth * 3}`)
    .attr('marker-end', `url(#${componentClass}__arrow-marker-end)`)
    .attr('stroke-width', strokeWidth)

  // Today dot
  const todayDot = svgContainer
    .append('circle')
    .attr('class', `${componentClass}__today-dot`)
    .attr('r', 5)

  // Time axis
  const xAxis = svgContainer
    .append('g')
    .attr('class', `${componentClass}__axis`)

  // Milestone Groups
  const milestoneDotGroup = svgContainer.append('g')
  const milestoneLineGroup = svgContainer.append('g')
  const milestoneLabelGroup = svgContainer.append('g')

  return {
    update (startDate, endDate, milestoneData) {
      const width = container.getBoundingClientRect().width

      const xPadding = 120

      const today = new Date()

      // Set the ranges and scale
      const x = d3.scaleTime().range([xPadding, width - xPadding])
      x.domain(d3.extent([startDate, endDate]))

      svgContainer
        .attr('height', height)
        .attr('width', width)

      // The past timeline
      svgContainer
        .select(`.${componentClass}__past-line`)
        .attr('x1', d => x(startDate))
        .attr('y1', d => height / 2)
        .attr('x2', d => x(today))
        .attr('y2', d => height / 2)

      // The future timeline
      svgContainer
        .select(`.${componentClass}__future-line`)
        .attr('x1', d => x(today))
        .attr('y1', d => height / 2)
        .attr('x2', d => x(endDate))
        .attr('y2', d => height / 2)

      // Today dot
      todayDot
        .attr('cx', d => x(today))
        .attr('cy', d => height / 2)

      const axisBottom = d3.axisBottom(x.nice(d3.utcMonth))
        .tickFormat(d3.timeFormat('%b %Y'))

      axisBottom.tickValues(getTickValues(startDate, endDate, width))

      xAxis
        .attr('transform', 'translate(0,' + height / 2 + ')')
        .call(axisBottom)

      // Axis Text
      xAxis
        .selectAll('text')
        .attr('dy', 15)
        .attr('class', `${componentClass}__axis-label`)

      // Hide Axis ticks and line
      xAxis.selectAll('line').remove()
      xAxis.selectAll('path').remove()

      const milestoneDots = milestoneDotGroup
        .selectAll('circle')
        .data(milestoneData)

      milestoneDots.enter()
        .append('circle')
        .merge(milestoneDots)
        .attr('class', `${componentClass}__milestone-dot`)
        .attr('r', 4)
        .attr('cx', d => x(d.date))
        .attr('cy', d => height / 2)

      milestoneDots.exit().remove()

      const milestoneLines = milestoneLineGroup
        .selectAll('line')
        .data(milestoneData)

      milestoneLines
        .enter()
        .append('line')
        .merge(milestoneLines)
        .attr('class', `${componentClass}__milestone-line`)
        .attr('stroke-width', 1)
        .attr('x1', d => x(d.date))
        .attr('y1', d => height / 2)
        .attr('x2', d => x(d.date))
        .attr('y2', (d, i) => (height / 2) + (40 * (i % 2 ? 1 : -1)))

      milestoneLines.exit().remove()

      const milestoneLabels = milestoneLabelGroup
        .selectAll('g')
        .data(milestoneData)

      // Add a group for each milestone label to wrap the text/rect
      const milestoneLabelsContainers = milestoneLabels.enter().append('g')
      // Add text
      milestoneLabelsContainers.append('text')
      // Add rect for the border
      milestoneLabelsContainers.append('rect')

      const milestoneLabelUpdate = milestoneLabelsContainers
        .merge(milestoneLabels)

      milestoneLabelUpdate
        .select('text')
        .attr('class', `${componentClass}__milestone-text`)
        .text(d => d.name)
        .attr('x', d => x(d.date) - 6)
        .attr('y', (d, i) => (height / 2) + (60 * (i % 2 ? 1 : -1)))
        .attr('dy', (d, i) => i % 2 ? 0 : 10)

      milestoneLabelUpdate
        .select('rect')
        .attr('class', `${componentClass}__milestone-text-box`)
        .attr('x', d => x(d.date) - 30)
        .attr('y', (d, i) => (height / 2) + (70 * (i % 2 ? 1 : -1)) - (i % 2 ? 30 : 0))
        .attr('rx', 15)
        .attr('ry', 15)
        .attr('width', (d, i, nodes) => {
          const siblingTextNode = nodes[i].previousElementSibling
          return siblingTextNode.getBoundingClientRect().width + 40
        })
        .attr('height', 30)

      milestoneLabels.exit().remove()
    }
  }
}

export default Component.extend({
  componentClass: 'c-programme-timeline',
  height: 160,

  didRender () {
    this._super(...arguments)
    console.log('didRender')
  },

  didInsertElement () {
    this._super(...arguments)

    console.log('didInsertElement')

    const startDate = this.startDate
    const endDate = this.endDate
    const milestones = [
      { date: startDate, name: 'Programme kick-off' },
      // @TODO Placeholder milestones
      { date: new Date(2019, 3, 1), name: 'Milestone 1' },
      { date: new Date(2019, 5, 1), name: 'Milestone 2' },
      { date: new Date(2019, 10, 1), name: 'Milestone 3' }
    ]

    const timeline = Timeline(this.element, this.componentClass)

    timeline.update(startDate, endDate, milestones)

    let resizeId
    $(window).resize(() => {
      clearTimeout(resizeId)
      resizeId = setTimeout(() => {
        timeline.update(startDate, endDate, milestones)
      }, 500)
    })
  }
})
