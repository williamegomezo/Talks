const ResponsiveImage = {
  name: 'ResponsiveImage',
  props: ['srcSet', 'alt'],
  data() {
    return {
      sizes: Object.keys(this.srcSet).filter(size => !!this.srcSet[size])
    }
  },
}

export default ResponsiveImage
