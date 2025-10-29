<script setup>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import FeedbackSection from '@/sections/FeedbackSection.vue';
</script>

<template>
    <main>
		<section>
			<Header />
		</section>
        <div style="min-width: 99vw; min-height: 100vh;">
            <RouterView />
        </div>
        <section>
			<FeedbackSection />
		</section>
		<section>
			<Footer />
		</section>
    </main>
</template>
