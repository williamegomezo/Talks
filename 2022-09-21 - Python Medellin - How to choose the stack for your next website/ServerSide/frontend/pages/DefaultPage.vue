<template>
  <pre>{{ page }}</pre>
</template>

<script>
export default {
  name: 'DefaultPage',
  asyncData(ctx) {
    const { page } = ctx.route?.matched?.[0]?.props?.default ?? {}
    return { page }
  },
}
</script>
