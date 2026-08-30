import { useRef, useState, type KeyboardEvent } from "react";

interface ChatInputProps {
  disabled: boolean;
  onSend: (message: string) => void;
}

function ChatInput({ disabled, onSend }: ChatInputProps) {
  const [value, setValue] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  function resize() {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${el.scrollHeight}px`;
  }

  function handleSend() {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;

    onSend(trimmed);
    setValue("");
    requestAnimationFrame(() => {
      if (textareaRef.current) textareaRef.current.style.height = "auto";
    });
  }

  function handleKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  }

  return (
    <div className="p-lg bg-surface-container/50 backdrop-blur-md border-t border-outline-variant/10 shrink-0">
      <div className="relative flex items-end gap-sm max-w-4xl mx-auto">
        <div className="flex-1 relative bg-surface-container-highest rounded-xl border border-outline-variant/20 focus-within:border-primary/50 focus-within:shadow-[0_0_15px_rgba(77,142,255,0.15)] transition-all duration-300">
          <textarea
            ref={textareaRef}
            value={value}
            onChange={(e) => {
              setValue(e.target.value);
              resize();
            }}
            onKeyDown={handleKeyDown}
            disabled={disabled}
            placeholder="Pergunte algo sobre o documento..."
            rows={1}
            className="w-full bg-transparent text-on-surface font-body-md text-body-md placeholder-on-surface-variant/50 p-md resize-none focus:outline-none max-h-32 min-h-[48px] overflow-hidden"
          />
        </div>
        <button
          type="button"
          onClick={handleSend}
          disabled={disabled || !value.trim()}
          className="p-md bg-primary text-on-primary rounded-xl hover:brightness-110 transition-all focus:outline-none focus:ring-2 focus:ring-primary/50 shadow-md flex items-center justify-center h-[48px] w-[48px] disabled:opacity-50"
        >
          <span
            className="material-symbols-outlined text-[20px]"
            style={{ fontVariationSettings: "'FILL' 1" }}
          >
            send
          </span>
        </button>
      </div>
      <div className="text-center mt-sm">
        <span className="font-label-sm text-label-sm text-on-surface-variant/50">
          Enter para enviar, Shift+Enter para nova linha
        </span>
      </div>
    </div>
  );
}

export default ChatInput;
