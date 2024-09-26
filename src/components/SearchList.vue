<template>
  <aside class="spaces-list" id="spaces-list">
    <div class="search">
      <input class="search__input" placeholder="Search..." />
      <button class="boxbutton boxbutton--darker close-search" aria-label="Close details">
        <svg class="icon icon--cross">
          <use xlink:href="#icon-cross"></use>
        </svg>
      </button>
    </div>
    <span class="label">
      <input id="sort-by-name" class="label__checkbox" type="checkbox" aria-label="Show alphabetically"/>
      <label class="label__text">A - Z</label>
    </span>
    <ul class="list grouped-by-category">
      <li
          v-for="(item, index) in spacesList"
          :key="index"
          class="list__item"
          :data-level="item.level"
          :data-category="item.category"
          :data-space="item.space"
      >
        <a href="#" class="list__link">{{ item.label }}</a>
      </li>
    </ul>
  </aside>
</template>

<script>
import levelData from "../descriptionData.json";

export default {
  data() {
    return {
      spacesList: levelData[0]["level0"].concat(levelData[0]["level1"], levelData[0]["level2"], levelData[0]["level3"])
    }
  }
}
</script>

<style scoped>
/* Add your CSS here */
</style>
