<script setup>
import { reactive } from 'vue';

const items = reactive([
  {
    title: "Apple Heart",
    space: 1.01,
    category: 1,
    openingHours: "6:30AM — 11:30PM",
    phone: "(0) 66 5738902",
    description: "Burdock celery - salsify, tomatillo. Bitter gourd horseradish leaves radicchio, celeriac miner's lettuce kurrat arugula fluted pumpkin turnip, arracacha water spinach nopal."
  },
  {
    title: "Crazy Banana",
    space: 1.02,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Apple Heart",
    space: 1.03,
    category: 2,
    openingHours: "6:30AM — 11:30PM",
    phone: "(0) 66 5738902",
    description: "Burdock celery - salsify, tomatillo. Bitter gourd horseradish leaves radicchio, celeriac miner's lettuce kurrat arugula fluted pumpkin turnip, arracacha water spinach nopal."
  },
  {
    title: "Crazy Banana",
    space: 1.04,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Apple Heart",
    space: 1.05,
    category: 4,
    openingHours: "6:30AM — 11:30PM",
    phone: "(0) 66 5738902",
    description: "Burdock celery - salsify, tomatillo. Bitter gourd horseradish leaves radicchio, celeriac miner's lettuce kurrat arugula fluted pumpkin turnip, arracacha water spinach nopal."
  },
  {
    title: "Crazy Banana",
    space: 1.06,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Apple Heart",
    space: 1.07,
    category: 1,
    openingHours: "6:30AM — 11:30PM",
    phone: "(0) 66 5738902",
    description: "Burdock celery - salsify, tomatillo. Bitter gourd horseradish leaves radicchio, celeriac miner's lettuce kurrat arugula fluted pumpkin turnip, arracacha water spinach nopal."
  },
  {
    title: "Crazy Banana",
    space: 1.08,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Apple Heart",
    space: 1.09,
    category: 1,
    openingHours: "6:30AM — 11:30PM",
    phone: "(0) 66 5738902",
    description: "Burdock celery - salsify, tomatillo. Bitter gourd horseradish leaves radicchio, celeriac miner's lettuce kurrat arugula fluted pumpkin turnip, arracacha water spinach nopal."
  },
  {
    title: "Crazy Banana",
    space: 2.01,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 2.02,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  // ... aut
  {
    title: "Crazy Banana",
    space: 2.03,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 2.04,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  // ... aut
  {
    title: "Crazy Banana",
    space: 2.05,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 2.06,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  // ... aut
  {
    title: "Crazy Banana",
    space: 2.07,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 2.08,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  // ... aut
  {
    title: "Crazy Banana",
    space: 3.01,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.02,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.03,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.04,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.05,
    category: 4,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.06,
    category: 4,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 3.07,
    category: 4,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.01,
    category: 1,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.02,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.03,
    category: 3,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.04,
    category: 4,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.05,
    category: 4,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.06,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
  {
    title: "Crazy Banana",
    space: 4.07,
    category: 2,
    openingHours: "7:30AM — 10:30PM",
    phone: "(0) 66 7822786",
    description: "Malva verticillata cichorium intybus zingiber officinale. Capsicum annuum Grossum group amorphophallus_paeoniifolius celosia argentea."
  },
]);
</script>

<template>
  <div v-for="item in items" :key="item.space" class="content__item" :data-space="item.space" :data-category="item.category">
    <h3 class="content__item-title">{{ item.title }}</h3>
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