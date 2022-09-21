import axios from "axios"
import ResponsiveImage from "~/components/ResponsiveImage/index.vue"

export default {
  name: 'HomePage',
  components: {
    ResponsiveImage,
  },
  data() {
    return {
      mainHeader:
        '', heroImageSrcSet: {}
    }
  },
  async fetch() {
    const pagesResponse = await axios.get(`${process.env.apiUrl}/api/v2/pages/?fields=*`)
    const pageMeta = pagesResponse.data.items.find(item => item.meta.relative_url === "/")
    const pageResponse = await axios.get(`${process.env.apiUrl}/api/v2/pages/${pageMeta.id}/`)
    const page = pageResponse.data
    this.mainHeader = page?.main_header;
    this.heroImageSrcSet = { ...page?.hero_image } || {};
  }
}
