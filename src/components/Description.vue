<script setup>
import levelData from "../descriptionData.json";

const items = levelData[0]["level0"].concat(levelData[0]["level1"], levelData[0]["level2"], levelData[0]["level3"]);
</script>

<template>
  <div v-for="item in items" :key="item.space" class="content__item" :data-space="item.space" :data-category="item.category">
    <h3 class="content__item-title">{{ item.label }}</h3>
    <div class="content__item-details">
      <p class="content__meta">
        <span class="content__meta-item"><strong>Opening Hours:</strong> {{ item.openingHours }}</span>
        <span class="content__meta-item"><strong>Phone:</strong> {{ item.phone }}</span>
      </p>
      <p class="content__desc">{{ item.description }}</p>
    </div>
  </div>
</template>

<style scoped>

</style>