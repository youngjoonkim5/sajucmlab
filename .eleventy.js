module.exports = function(eleventyConfig) {
  // Auto-tag all src/posts/*.md as 'post' so collections.post works
  eleventyConfig.addCollection("post", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/posts/*.md");
  });

  // ISO 8601 date filter for Nunjucks templates (e.g. sitemap.njk)
  eleventyConfig.addFilter("dateToIso", function(date) {
    if (!date) return new Date().toISOString();
    var d = (date instanceof Date) ? date : new Date(date);
    return d.toISOString();
  });

  eleventyConfig.addFilter("jsonify", function(value) {
    return JSON.stringify(value, null, 2);
  });

  // Pass through static assets (images, fonts, etc.) to the output
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
};
