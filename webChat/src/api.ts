const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export interface UploadedDocument {
  id: string;
  filename: string;
  status: string;
}

export async function uploadDocument(file: File): Promise<UploadedDocument> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_URL}/documents`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const detail = await safeErrorDetail(response);
    throw new Error(detail ?? `Upload failed (${response.status})`);
  }

  return response.json();
}

export async function askQuestion(userPrompt: string): Promise<string> {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ userPrompt }),
  });

  if (!response.ok) {
    const detail = await safeErrorDetail(response);
    throw new Error(detail ?? `Chat request failed (${response.status})`);
  }

  const data: { answer: string } = await response.json();
  return data.answer;
}

async function safeErrorDetail(response: Response): Promise<string | null> {
  try {
    const data = await response.json();
    return typeof data.detail === "string" ? data.detail : null;
  } catch {
    return null;
  }
}
