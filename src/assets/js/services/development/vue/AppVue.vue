<script setup lang="ts">
type Prop = {
  val1: string;
};

defineProps<Prop>();
</script>

<template>
  <div class="bg-blue-300 p-10">
    Vue Test

    <div>val1: {{ val1 }}</div>
  </div>
</template>
