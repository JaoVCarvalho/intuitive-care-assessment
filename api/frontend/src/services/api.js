const BASE_URL = "http://127.0.0.1:8000"; 

export async function searchByName(query) {
  try {
    const response = await fetch(`${BASE_URL}/search/name?query=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error("Failed to fetch by name");
    return await response.json();
  } catch (error) {
    console.error("Error searching by name:", error);
    return [];
  }
}

export async function searchByAnsCode(query) {
  try {
    const response = await fetch(`${BASE_URL}/search/ans-code?query=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error("Failed to fetch by ANS code");
    return await response.json();
  } catch (error) {
    console.error("Error searching by ANS code:", error);
    return [];
  }
}

export async function searchByCnpj(query) {
  try {
    const response = await fetch(`${BASE_URL}/search/cnpj?query=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error("Failed to fetch by CNPJ");
    return await response.json();
  } catch (error) {
    console.error("Error searching by CNPJ:", error);
    return [];
  }
}
