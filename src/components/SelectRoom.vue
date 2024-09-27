<script>
export default {
  data() {
    return {
      selectedOption1: null,
      selectedOption2: null,
      options1: ['Option 1A', 'Option 1B', 'Option 1C'],
      options2: ['Option 2A', 'Option 2B', 'Option 2C']
    };
  }
};
</script>

<template>
  <div class="select-room">
    <label for="dropdown1">Select Option 1:</label>
    <select v-model="selectedOption1" id="dropdown1">
      <option v-for="option in options1" :key="option" :value="option">{{ option }}</option>
    </select>

    <label for="dropdown2">Select Option 2:</label>
    <select v-model="selectedOption2" id="dropdown2">
      <option v-for="option in options2" :key="option" :value="option">{{ option }}</option>
    </select>

    <p>Selected Option 1: {{ selectedOption1 }}</p>
    <p>Selected Option 2: {{ selectedOption2 }}</p>
  </div>
</template>

<style scoped>
.select-room {
  position: absolute;
  bottom: 0;
  left: 0;
  z-index: 51564156165541;
}
</style>
