import ResponsiveImage from "~/components/ResponsiveImage/index.vue"

export default {
    name: 'HomePage',
    components: {
      ResponsiveImage,
    },
    data() {
        const { page } = this.$route?.matched?.[0]?.props?.default ?? {}
        const mainHeader = page?.main_header;
        const heroImageSrcSet = page?.hero_image;

        return {
          mainHeader, heroImageSrcSet
        }
    },
}
