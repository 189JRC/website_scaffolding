<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="mt-5 p-6 max-w-sm mx-auto dark:bg-gray-800 rounded-xl shadow-md flex items-center space-x-4">
    <div class="flex-shrink-0">
      <img class="h-12 w-12" src="/vite.svg" alt="ChitChat Logo">
    </div>
    <div>
      <div class="text-xl font-medium dark:text-white">ChitChat</div>
      <p class="dark:text-gray-300">You have a new message!</p>
    </div>
  </div>

  <div
    class="mt-5 p-6 max-w-sm mx-auto dark:bg-gray-700 rounded-xl shadow-md flex justify-between items-center space-x-4">
    <div>
      <div class="text-xl font-medium dark:text-white">ChitChat</div>
      <p class="dark:text-gray-300">You have a new message!</p>
    </div>
    <div class="flex-shrink-0">
      <img class="h-12 w-12" src="./assets/vue.svg" alt="ChitChat Logo">
    </div>
  </div>



  <div
    class="mt-5 p-6 max-w-sm mx-auto dark:bg-gray-600 rounded-xl shadow-md ">
  <HelloWorld msg="Website Scaffolding" />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
