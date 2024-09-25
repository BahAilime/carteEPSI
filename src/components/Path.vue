<script>
export default {
  props: {
    coordinates: {
      type: Array,
      required: true
    },
    imageSize: {
      type: Array,
      default: () => [3135, 1444]
    }
  },
  mounted() {
    // Dessiner le chemin après que le composant soit monté
    this.drawPath();
  },
  watch: {
    coordinates: {
      handler() {
        // Redessiner le chemin si les coordonnées changent
        this.drawPath();
      },
      deep: true
    }
  },
  methods: {
    drawPath() {
      const canvas = this.$refs.pathCanvas;
      const ctx = canvas.getContext('2d');

      ctx.clearRect(0, 0, canvas.width, canvas.height);

      ctx.beginPath();
      for (let i = 0; i < this.coordinates.length - 1; i++) {
        const start = this.coordinates[i];
        const end = this.coordinates[i + 1];
        ctx.moveTo(start[0], start[1]);
        ctx.lineTo(end[0], end[1]);
      }
      ctx.strokeStyle = 'rgba(255, 104, 107, 1)';
      ctx.lineWidth = 15;
      ctx.stroke();
    }
  }
}
</script>

<template>
  <div class="path">
    <canvas class="path" ref="pathCanvas"  :width="imageSize[0]" :height="imageSize[1]"></canvas>
  </div>
</template>

<style scoped>
.path {
  width: 100%;
  height: 100%;
  position: absolute;
}
</style>