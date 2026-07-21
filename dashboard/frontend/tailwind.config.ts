import type { Config } from "tailwindcss";
const config: Config = { content: ["./pages/**/*.{ts,tsx}"], theme: { extend: { colors: { ink: "#050a12", panel: "#09111f", line: "#17243a", violet: "#7c3cff", cyan: "#08d9ff", lime: "#26e36a", amber: "#f3b21b", rose: "#ff3d77" } } }, plugins: [] };
export default config;
